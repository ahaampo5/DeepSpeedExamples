from .raw_datasets import PromptRawDataset

class AceReasoningDataset(PromptRawDataset):
    """
    Ace Reasoning dataset for supervised fine-tuning.
    This dataset is used for training models on reasoning tasks.
    """

    def __init__(self, output_path, seed, local_rank, dataset_name):
        super().__init__(output_path, seed, local_rank, dataset_name)
        self.dataset_name = "nvidia/AceReason-1.1-SFT"
        self.dataset_name_clean = "nvidia_AceReason-1.1-SFT"
        
    def get_train_data(self):
        return self.raw_datasets["train"]

    def get_eval_data(self):
        return self.raw_datasets["train"].select(range(100))

    def get_prompt(self, sample):
        return sample["input"]

    def get_chosen(self, sample):
        return sample["output"]

    def get_rejected(self, sample):
        return ""

    def get_prompt_and_chosen(self, sample):
        return sample["input"] + sample["output"]

    def get_prompt_and_rejected(self, sample):
        return sample["input"] + ""