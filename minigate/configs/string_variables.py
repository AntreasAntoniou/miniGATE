from dataclasses import dataclass

DATASET_DIR = "${data_dir}"
SEED = "${seed}"
ROOT_EXPERIMENT_DIR = "${root_experiment_dir}"
CURRENT_EXPERIMENT_DIR = "${current_experiment_dir}"
CODE_DIR = "${code_dir}"
EXPERIMENT_NAME = "${name}"
BATCH_SIZE = "${batch_size}"
NUM_TRAIN_SAMPLES = "${num_train_samples}"
CHECKPOINT_DIR = "${current_experiment_dir}/checkpoints/"
ADDITIONAL_INPUT_TRANSFORMS = "${additional_input_transforms}"
ADDITIONAL_TARGET_TRANSFORMS = "${additional_target_transforms}"


@dataclass
class MaxDurationTypes:
    MAX_EPOCHS: str = "${trainer.max_epochs}"
    MAX_STEPS: str = "${trainer.max_steps}"
