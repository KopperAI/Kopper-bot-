from pyVintedVN.items import Items


class Vinted:
    """
    This class is built to connect with the Vinted API.

    It serves as a wrapper around the Items class, providing a convenient interface
    for searching Vinted listings with optional proxy support.

    Attributes:
        items (Items): Une instance de la classe Items pour la recherche des listes Vinted.

    Example:
        >>> vinted = Vinted()
        >>> items = vinted.items.search("https://www.vinted.fr/catalog?search_text=shoes")
    """

    def __init__(self):
        """
        Initialiser la classe Vinted avec des paramètres de proxy optionnels.

        Args: None
        """

        # Initialize Items instance for searching Vinted listings
        self.items = Items()