# pylint: disable=too-few-public-methods
"""
    Kivy Networkstat UI test
"""

from .telenium_process import TeleniumTestProcess


class NetworkStatusScreen(TeleniumTestProcess):
    """NetworkStatus Screen Functionality Testing"""

    def test_network_status(self):
        """Show NetworkStatus"""
        # This is for checking Current screen
        self.assert_wait_no_except('//ScreenManager[@current]', timeout=15, value='inbox')
        # Method to open side navbar
        # due to rapid transition effect, it doesn't click on menu-bar
        self.open_side_navbar()
        # this is for scrolling Nav drawer
        self.drag("//NavigationItem[@text=\"Sent\"]", "//NavigationItem[@text=\"Inbox\"]")
        # assert for checking scroll function
        self.assertCheckScrollDown('//ContentNavigationDrawer//ScrollView[0]', timeout=5)
