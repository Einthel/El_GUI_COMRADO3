# widget_registry.py

from Bar_widget import ClockWidget, VolumeWidget, MusicWidget, TimerWidget, TestWidget

WIDGET_REGISTRY = {
    "ClockWidget": ClockWidget,
    "VolumeWidget": VolumeWidget,
    "MusicWidget": MusicWidget,
    "TimerWidget": TimerWidget,
    "TestWidget": TestWidget,
    # При добавлении нового виджета его нужно будет просто
    # импортировать и добавить в этот словарь.
}

def get_widget_class(class_name: str):
    """
    Safely retrieves a widget class from the registry by its name.
    Returns the class if found, otherwise None.
    """
    return WIDGET_REGISTRY.get(class_name)
