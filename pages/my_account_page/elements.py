from core.form_element import FormElement


class MyAccountPageEle:
    lnk_my_account_page = FormElement("CSS_SELECTOR", "a[href*='my-account']", "My Account")
    lnk_addresses_page = FormElement("CSS_SELECTOR", "a[href*='edit-address']", "Addresses")

    menu_ele = FormElement("ID", "menu-icon", "")
    register_email_ele = FormElement("ID", "reg_email", "")
    register_pw_ele = FormElement("ID", "reg_password", "")
    register_button_ele = FormElement("NAME", "register", "")
    logout_ele = FormElement("CSS_SELECTOR", "a[href*='customer-logout']", "Logout")
    login_account_ele = FormElement("ID", "username", "")
    login_pw_ele = FormElement("ID", "password", "")
    login_button_ele = FormElement("NAME", "login", "")

    billing_edit_page = FormElement("CSS_SELECTOR", "a[href*='billing']", "Edit")
    billing_first_name_ele = FormElement("ID", "billing_first_name", "")
    billing_last_name_ele = FormElement("ID", "billing_last_name", "")
    billing_phone_ele = FormElement("ID", "billing_phone", "")
    billing_country_ele = FormElement("ID", "select2-chosen-1", "")
    billing_country_search_ele = FormElement("ID", "s2id_autogen1_search", "")
    billing_country_select_ele = FormElement("CLASS_NAME", "select2-match", "")
    billing_address_ele = FormElement("ID", "billing_address_1", "")
    billing_city_ele = FormElement("ID", "billing_city", "")
    billing_state_ele = FormElement("ID", "select2-chosen-2", "")
    billing_state_search_ele = FormElement("ID", "s2id_autogen2_search", "")
    billing_state_select_ele = FormElement("CLASS_NAME", "select2-match", "")
    billing_postcode_ele = FormElement("ID", "billing_postcode", "")
    billing_info_ele = FormElement("CLASS_NAME", "u-column1.col-1.woocommerce-Address", "")

    shipping_edit_page = FormElement("CSS_SELECTOR", "a[href*='shipping']", "Edit")
    shipping_first_name_ele = FormElement("ID", "shipping_first_name", "")
    shipping_last_name_ele = FormElement("ID", "shipping_last_name", "")
    shipping_country_ele = FormElement("ID", "select2-chosen-1", "")
    shipping_country_search_ele = FormElement("ID", "s2id_autogen1_search", "")
    shipping_country_select_ele = FormElement("CLASS_NAME", "select2-match", "")
    shipping_address_ele = FormElement("ID", "shipping_address_1", "")
    shipping_city_ele = FormElement("ID", "shipping_city", "")
    shipping_state_ele = FormElement("ID", "select2-chosen-2", "")
    shipping_state_search_ele = FormElement("ID", "s2id_autogen2_search", "")
    shipping_state_select_ele = FormElement("CLASS_NAME", "select2-match", "")
    shipping_postcode_ele = FormElement("ID", "shipping_postcode", "")
    shipping_info_ele = FormElement("CLASS_NAME", "u-column2.col-2.woocommerce-Address", "")

    save_button_ele = FormElement("NAME", "save_address", "Save Address")
