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
        return self.raw_datasets["train"].select(range(1000))

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
    
# FreedomIntelligence/medical-o1-reasoning-SFT
class MedicalReasoningDataset(PromptRawDataset):
    """
    Medical Reasoning dataset for supervised fine-tuning.
    This dataset is used for training models on medical reasoning tasks.
    """

    def __init__(self, output_path, seed, local_rank, dataset_name):
        super().__init__(output_path, seed, local_rank, dataset_name)
        self.dataset_name = "FreedomIntelligence/medical-o1-reasoning-SFT"
        self.dataset_name_clean = "FreedomIntelligence_medical-o1-reasoning-SFT"
        
    def get_train_data(self):
        return self.raw_datasets["train"]

    def get_eval_data(self):
        return self.raw_datasets["train"].select(range(100))

    def get_prompt(self, sample):
        return sample["Question"]

    def get_chosen(self, sample):
        return sample["Complex_CoT"] + sample["Response"]

    def get_rejected(self, sample):
        return ""

    def get_prompt_and_chosen(self, sample):
        return sample["Question"] + sample["Complex_CoT"] + sample["Response"]

    def get_prompt_and_rejected(self, sample):
        return sample["Question"] + ""
    

###################################### Reasoning 360 Datasets ######################################
class LeetcodeDataset(PromptRawDataset):
    """
    Leetcode dataset for supervised fine-tuning.
    This dataset is used for training models on coding tasks.
    """

    def __init__(self, output_path, seed, local_rank, dataset_name):
        super().__init__(output_path, seed, local_rank, dataset_name)
        self.dataset_name = "/root/workspace/DeepSpeedExamples/data/train/codegen__leetcode2k_1.3k.parquet"
        self.dataset_name_clean = "codegen_leetcode2k-1.3k"
        
    def get_train_data(self):
        return self.raw_datasets

    def get_eval_data(self):
        return self.raw_datasets.select(range(100))

    def get_prompt(self, sample):
        return sample["query"]

    def get_chosen(self, sample):
        return sample["response"]

    def get_rejected(self, sample):
        return ""

    def get_prompt_and_chosen(self, sample):
        return sample["query"] + sample["response"]

    def get_prompt_and_rejected(self, sample):
        return sample["query"] + ""