from PySide6.QtCore import QObject, Signal

class PageManager(QObject):
    """Manages page state and navigation logic."""
    page_changed = Signal(int) # Signal emitting the new page number (1-indexed)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._page_keys = []
        self.current_page_index = 0

    def set_page_keys(self, page_keys):
        """Updates the list of page keys and resets the index if needed."""
        self._page_keys = sorted(page_keys) if page_keys else []
        # Reset index if it's out of bounds after updating keys
        if self.current_page_index >= len(self._page_keys):
            # Go to the last page if it exists, otherwise 0
            self.current_page_index = max(0, len(self._page_keys) - 1)

    def get_page_count(self):
        """Returns the total number of pages."""
        return len(self._page_keys)

    def get_current_page_number(self):
        """Returns the current page number (1-indexed)."""
        if self.get_page_count() == 0:
            return 0
        return self.current_page_index + 1

    def get_page_label_text(self):
        """Returns the text for the page label, e.g., '1/3'."""
        page_count = self.get_page_count()
        current_page = self.get_current_page_number() if page_count > 0 else 0
        return f"{current_page}/{page_count}"

    def next(self):
        """Switches to the next page, cycling to the start if at the end."""
        page_count = self.get_page_count()
        if page_count == 0:
            return
        
        self.current_page_index = (self.current_page_index + 1) % page_count
        self.page_changed.emit(self.get_current_page_number())

    def previous(self):
        """Switches to the previous page, cycling to the end if at the start."""
        page_count = self.get_page_count()
        if page_count == 0:
            return
            
        self.current_page_index = (self.current_page_index - 1 + page_count) % page_count
        self.page_changed.emit(self.get_current_page_number())

    def go_to_page(self, page_number):
        """
        Switches to a specific page number (1-indexed).
        Emits the page_changed signal.
        """
        page_index = page_number - 1
        if 0 <= page_index < self.get_page_count():
            if self.current_page_index != page_index:
                self.current_page_index = page_index
            self.page_changed.emit(self.get_current_page_number())

    def get_key_for_index(self, index):
        """Returns the page key for a given index."""
        if 0 <= index < len(self._page_keys):
            return self._page_keys[index]
        return None
