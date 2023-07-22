from pages.dynamic_properties import DynamicPropertiesPage


class TestDynamicProperties:

    def test_enable_button(self):
        dynamic_properties_page = DynamicPropertiesPage()
        dynamic_properties_page.wait_for_enable_button()

    def test_color_changeable_button(self):
        dynamic_properties_page = DynamicPropertiesPage()
        dynamic_properties_page.wait_for_color_changeable_button()

    def test_visible_button(self):
        dynamic_properties_page = DynamicPropertiesPage()
        dynamic_properties_page.wait_for_visible_button()