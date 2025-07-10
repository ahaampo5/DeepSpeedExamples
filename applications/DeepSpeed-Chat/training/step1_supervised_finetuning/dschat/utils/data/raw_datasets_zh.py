# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

import os
# DeepSpeed Team
from datasets import load_dataset, load_from_disk
from torch.utils.data import Subset
import re


# The template prompt dataset class that all new dataset porting needs to
# follow in order to have a unified API and unified data format.
class PromptRawDataset(object):

    def __init__(self, output_path, seed, local_rank, dataset_name):
        self.output_path = output_path
        self.seed = seed
        self.local_rank = local_rank
        if os.path.exists(dataset_name):
            self.raw_datasets = load_from_disk(dataset_name)
        elif not dataset_name == 'local/jsonfile':
            self.raw_datasets = load_dataset(dataset_name)

    def get_train_data(self):
        return

    def get_eval_data(self):
        return

    # The prompt should be in the format of: " Human: " + actual_prompt_sentence + " Assistant:"
    def get_prompt(self, sample):
        return

    # The chosen response should be in the format of: " " + actual_response_sentence
    def get_chosen(self, sample):
        return

    # The rejected response should be in the format of: " " + actual_response_sentence
    # If the dataset does not have rejected response, return None
    def get_rejected(self, sample):
        return

    def get_prompt_and_chosen(self, sample):
        return

    def get_prompt_and_rejected(self, sample):
        return


# English dataset
class HuggingFaceTB_SmoltalkDataset_ZH(PromptRawDataset):

    def __init__(self, output_path, seed, local_rank, dataset_name):
        super().__init__(output_path, seed, local_rank, dataset_name)
        self.dataset_name = "mncai/foundation_model_smoltalk_ko_translate"
        self.dataset_name_clean = "HuggingFaceTB_SmoltalkDataset_KO"

    def get_train_data(self):
        return self.raw_datasets["train"]

    def get_eval_data(self):
        return self.raw_datasets["train"].select(range(0))

    def get_prompt(self, sample):
        return sample["messages"][:-1]

    def get_chosen(self, sample):
        return sample["messages"][-1:]

    def get_rejected(self, sample):
        return ""

    def get_prompt_and_chosen(self, sample):
        return sample["messages"]

    def get_prompt_and_rejected(self, sample):
        return sample["messages"] + ""
