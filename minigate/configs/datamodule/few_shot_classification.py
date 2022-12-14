from dataclasses import dataclass
from typing import Any

from minigate.configs import get_module_import_path
from minigate.configs.datamodule.base import DataLoaderConfig
from minigate.configs.datasets.few_shot_datasets import *
from minigate.configs.string_variables import DATASET_DIR, NUM_TRAIN_SAMPLES
from minigate.configs.transforms.transforms import *
from minigate.datamodules.tf_hub.few_shot_episodic_sets import FewShotDataModule


@dataclass
class FewShotDataModuleConfig:
    """
    Class for configuring a few shot datamodule
    """

    dataset_config: FewShotDatasetConfig
    data_loader_config: DataLoaderConfig
    transform_train: FewShotTransformConfig
    transform_eval: FewShotTransformConfig
    train_num_episodes: int = 1000
    eval_num_episodes: int = 600

    _target_: str = get_module_import_path(FewShotDataModule)


@dataclass
class OmniglotFewShotDataModuleConfig(FewShotDataModuleConfig):
    dataset_config: OmniglotFewShotDatasetConfig = OmniglotFewShotDatasetConfig(
        dataset_root=DATASET_DIR
    )
    data_loader_config: DataLoaderConfig = DataLoaderConfig()
    transform_train: Any = FewShotTransformConfig(
        support_set_input_transform=OmniglotSupportSetTransformConfig(),
        query_set_input_transform=OmniglotQuerySetTransformConfig(),
    )
    transform_eval: Any = FewShotTransformConfig(
        support_set_input_transform=OmniglotSupportSetTransformConfig(),
        query_set_input_transform=OmniglotQuerySetTransformConfig(),
    )
    _target_: str = get_module_import_path(FewShotDataModule)


@dataclass
class CUB200FewShotDataModuleConfig(FewShotDataModuleConfig):
    dataset_config: CUB200FewShotDatasetConfig = CUB200FewShotDatasetConfig(
        dataset_root=DATASET_DIR
    )
    data_loader_config: DataLoaderConfig = DataLoaderConfig()
    transform_train: Any = FewShotTransformConfig(
        support_set_input_transform=CUB200SupportSetTransformConfig(),
        query_set_input_transform=CUB200QuerySetTransformConfig(),
    )
    transform_eval: Any = FewShotTransformConfig(
        support_set_input_transform=CUB200SupportSetTransformConfig(),
        query_set_input_transform=CUB200QuerySetTransformConfig(),
    )


@dataclass
class AircraftFewShotDataModuleConfig(FewShotDataModuleConfig):
    dataset_config: AircraftFewShotDatasetConfig = AircraftFewShotDatasetConfig(
        dataset_root=DATASET_DIR
    )
    data_loader_config: DataLoaderConfig = DataLoaderConfig()
    transform_train: Any = FewShotTransformConfig(
        support_set_input_transform=AircraftSupportSetTransformConfig(),
        query_set_input_transform=AircraftQuerySetTransformConfig(),
    )
    transform_eval: Any = FewShotTransformConfig(
        support_set_input_transform=AircraftSupportSetTransformConfig(),
        query_set_input_transform=AircraftQuerySetTransformConfig(),
    )


@dataclass
class DTDFewShotDataModuleConfig(FewShotDataModuleConfig):
    dataset_config: DTDFewShotDatasetConfig = DTDFewShotDatasetConfig(
        dataset_root=DATASET_DIR
    )
    data_loader_config: DataLoaderConfig = DataLoaderConfig()
    transform_train: Any = FewShotTransformConfig(
        support_set_input_transform=DTDSupportSetTransformConfig(),
        query_set_input_transform=DTDQuerySetTransformConfig(),
    )
    transform_eval: Any = FewShotTransformConfig(
        support_set_input_transform=DTDSupportSetTransformConfig(),
        query_set_input_transform=DTDQuerySetTransformConfig(),
    )


@dataclass
class GermanTrafficSignsFewShotDataModuleConfig(FewShotDataModuleConfig):
    dataset_config: GermanTrafficSignsFewShotDatasetConfig = (
        GermanTrafficSignsFewShotDatasetConfig(dataset_root=DATASET_DIR)
    )
    data_loader_config: DataLoaderConfig = DataLoaderConfig()
    transform_train: Any = FewShotTransformConfig(
        support_set_input_transform=GermanTrafficSignsSupportSetTransformConfig(),
        query_set_input_transform=GermanTrafficSignsQuerySetTransformConfig(),
    )
    transform_eval: Any = FewShotTransformConfig(
        support_set_input_transform=GermanTrafficSignsSupportSetTransformConfig(),
        query_set_input_transform=GermanTrafficSignsQuerySetTransformConfig(),
    )


@dataclass
class QuickDrawFewShotDataModuleConfig(FewShotDataModuleConfig):
    dataset_config: QuickDrawFewShotDatasetConfig = QuickDrawFewShotDatasetConfig(
        dataset_root=DATASET_DIR
    )
    data_loader_config: DataLoaderConfig = DataLoaderConfig()
    transform_train: Any = FewShotTransformConfig(
        support_set_input_transform=QuickDrawSupportSetTransformConfig(),
        query_set_input_transform=QuickDrawQuerySetTransformConfig(),
    )
    transform_eval: Any = FewShotTransformConfig(
        support_set_input_transform=QuickDrawSupportSetTransformConfig(),
        query_set_input_transform=QuickDrawQuerySetTransformConfig(),
    )


@dataclass
class VGGFlowersFewShotDataModuleConfig(FewShotDataModuleConfig):
    dataset_config: VGGFlowersFewShotDatasetConfig = VGGFlowersFewShotDatasetConfig(
        dataset_root=DATASET_DIR
    )
    data_loader_config: DataLoaderConfig = DataLoaderConfig()
    transform_train: Any = FewShotTransformConfig(
        support_set_input_transform=VGGFlowersSupportSetTransformConfig(),
        query_set_input_transform=VGGFlowersQuerySetTransformConfig(),
    )
    transform_eval: Any = FewShotTransformConfig(
        support_set_input_transform=VGGFlowersSupportSetTransformConfig(),
        query_set_input_transform=VGGFlowersQuerySetTransformConfig(),
    )


@dataclass
class FungiFewShotDataModuleConfig(FewShotDataModuleConfig):
    dataset_config: FungiFewShotDatasetConfig = FungiFewShotDatasetConfig(
        dataset_root=DATASET_DIR
    )
    data_loader_config: DataLoaderConfig = DataLoaderConfig()
    transform_train: Any = FewShotTransformConfig(
        support_set_input_transform=FungiSupportSetTransformConfig(),
        query_set_input_transform=FungiQuerySetTransformConfig(),
    )
    transform_eval: Any = FewShotTransformConfig(
        support_set_input_transform=FungiSupportSetTransformConfig(),
        query_set_input_transform=FungiQuerySetTransformConfig(),
    )


@dataclass
class MSCOCOFewShotDataModuleConfig(FewShotDataModuleConfig):
    dataset_config: MSCOCOFewShotDatasetConfig = MSCOCOFewShotDatasetConfig(
        dataset_root=DATASET_DIR
    )
    data_loader_config: DataLoaderConfig = DataLoaderConfig()
    transform_train: Any = FewShotTransformConfig(
        support_set_input_transform=MSCOCOSupportSetTransformConfig(),
        query_set_input_transform=MSCOCOQuerySetTransformConfig(),
    )
    transform_eval: Any = FewShotTransformConfig(
        support_set_input_transform=MSCOCOSupportSetTransformConfig(),
        query_set_input_transform=MSCOCOQuerySetTransformConfig(),
    )
