from dataclasses import dataclass
from typing import Any, Optional

from minigate.configs import get_module_import_path


@dataclass
class FewShotDatasetConfig:
    """
    Class for configuring a few shot dataset
    """

    from minigate.datasets.tf_hub.few_shot.base import FewShotClassificationDatasetTFDS

    dataset_root: str
    split_name: Optional[str] = None
    download: bool = True
    num_episodes: int = 600
    min_num_classes_per_set: int = 5
    min_num_samples_per_class: int = 2
    num_classes_per_set: int = 25  # n_way
    num_samples_per_class: int = 10  # n_shot
    variable_num_samples_per_class: bool = True
    variable_num_classes_per_set: bool = True
    support_set_input_transform: Any = None
    query_set_input_transform: Any = None
    support_set_target_transform: Any = None
    query_set_target_transform: Any = None
    support_to_query_ratio: float = 0.75
    rescan_cache: bool = False
    _target_: Any = FewShotClassificationDatasetTFDS


@dataclass
class OmniglotFewShotDatasetConfig(FewShotDatasetConfig):
    """
    Class for configuring a few shot dataset
    """

    from minigate.datasets.tf_hub.few_shot.omniglot import (
        OmniglotFewShotClassificationDataset,
    )

    _target_: Any = get_module_import_path(OmniglotFewShotClassificationDataset)


@dataclass
class CUB200FewShotDatasetConfig(FewShotDatasetConfig):
    """
    Class for configuring a few shot dataset
    """

    from minigate.datasets.tf_hub.few_shot.cu_birds import (
        CUB200FewShotClassificationDataset,
    )

    _target_: Any = get_module_import_path(CUB200FewShotClassificationDataset)


@dataclass
class AircraftFewShotDatasetConfig(FewShotDatasetConfig):
    """
    Class for configuring a few shot dataset
    """

    from minigate.datasets.tf_hub.few_shot.aircraft import (
        AircraftFewShotClassificationDataset,
    )

    _target_: Any = get_module_import_path(AircraftFewShotClassificationDataset)


@dataclass
class DTDFewShotDatasetConfig(FewShotDatasetConfig):
    """
    Class for configuring a few shot dataset
    """

    from minigate.datasets.tf_hub.few_shot.dtd import DTDFewShotClassificationDataset

    _target_: Any = get_module_import_path(DTDFewShotClassificationDataset)


@dataclass
class GermanTrafficSignsFewShotDatasetConfig(FewShotDatasetConfig):
    """
    Class for configuring a few shot dataset
    """

    from minigate.datasets.tf_hub.few_shot.german_traffic_signs import (
        GermanTrafficSignsFewShotClassificationDataset,
    )

    _target_: Any = get_module_import_path(
        GermanTrafficSignsFewShotClassificationDataset
    )


@dataclass
class VGGFlowersFewShotDatasetConfig(FewShotDatasetConfig):
    """
    Class for configuring a few shot dataset
    """

    from minigate.datasets.tf_hub.few_shot.vgg_flowers import (
        VGGFlowersFewShotClassificationDataset,
    )

    _target_: Any = get_module_import_path(VGGFlowersFewShotClassificationDataset)


@dataclass
class QuickDrawFewShotDatasetConfig(FewShotDatasetConfig):
    """
    Class for configuring a few shot dataset
    """

    from minigate.datasets.tf_hub.few_shot.quickdraw import (
        QuickDrawFewShotClassificationDataset,
    )

    _target_: Any = get_module_import_path(QuickDrawFewShotClassificationDataset)


@dataclass
class FungiFewShotDatasetConfig(FewShotDatasetConfig):
    """
    Class for configuring a few shot dataset
    """

    from minigate.datasets.learn2learn_hub.few_shot.fungi import (
        FungiFewShotClassificationDataset,
    )

    _target_: Any = get_module_import_path(FungiFewShotClassificationDataset)


@dataclass
class MSCOCOFewShotDatasetConfig(FewShotDatasetConfig):
    """
    Class for configuring a few shot dataset
    """

    from minigate.datasets.tf_hub.few_shot.mscoco import (
        MSCOCOFewShotClassificationDataset,
    )

    _target_: Any = get_module_import_path(MSCOCOFewShotClassificationDataset)
