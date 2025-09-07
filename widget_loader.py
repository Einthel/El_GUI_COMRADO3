# widget_loader.py

import warnings
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt

from LoadSave import load_bar_config
from widget_registry import get_widget_class
import constants

def clear_layout(layout):
    """Removes all widgets from a layout."""
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

def clear_target_frames(target_frames):
    """Clears all widgets from the provided target frames."""
    for target_frame in target_frames:
        # Using findChildren to find all QWidget children
        for child in target_frame.findChildren(QWidget):
            # Ensure we only delete direct children
            if child.parent() == target_frame:
                child.deleteLater()


def load_and_display_widgets(parent_widget, is_editor=False):
    """
    Loads widget configuration and displays widgets on the parent.

    :param parent_widget: The parent widget (e.g., MainWindow.ui or EditorBarWindow.ui)
                          where target frames are located.
    :param is_editor: Boolean flag to determine which set of target names to use.
    """
    # 1. Clear existing widgets
    target_names = []
    for i in range(1, 6):
        base_name = "Bar_target_"
        if is_editor:
            base_name = "Bar_editor_target_"
        target_names.append(f"{base_name}{i}")

    target_frames = [getattr(parent_widget, name, None) for name in target_names]
    target_frames = [frame for frame in target_frames if frame is not None] # Filter out non-existent frames
    
    clear_target_frames(target_frames)

    # 2. Load config
    config = load_bar_config()
    if not config:
        return

    # 3. Iterate and create widgets
    for target_name, widget_data in config.items():
        if not isinstance(widget_data, dict):
            warnings.warn(f"Invalid entry for '{target_name}' in config_bar.json. Skipping.")
            continue

        widget_type = widget_data.get(constants.KEY_WIDGET_TYPE)
        widget_settings = widget_data.get(constants.KEY_WIDGET_SETTINGS, {})
        
        if not widget_type:
            continue
        
        # Determine the correct target frame on the main window or editor
        main_target_name = target_name if is_editor else target_name.replace("_editor", "")
        target_frame = getattr(parent_widget, main_target_name, None)
        
        if not target_frame:
            warnings.warn(f"Slot '{main_target_name}' not found in the parent widget.")
            continue

        WidgetClass = get_widget_class(widget_type)
        if not WidgetClass:
            warnings.warn(f"Widget class '{widget_type}' not found in the registry.")
            continue

        # Create the widget with its settings
        new_widget = WidgetClass(parent=target_frame, settings=widget_settings)
        new_widget.setWindowFlags(Qt.Widget)

        # In the main window, dragging is disabled. In the editor, it's enabled.
        if hasattr(new_widget, 'setDraggable'):
             new_widget.setDraggable(is_editor) 
        
        # Apply position from settings
        position = widget_settings.get(constants.KEY_WIDGET_POSITION, [0, 0])
        new_widget.move(position[0], position[1])
        
        try:
            new_widget.setObjectName(widget_type)
        except Exception:
            pass # Some widgets might not support it
        
        new_widget.show()
