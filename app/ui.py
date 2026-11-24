from m3_ext.ui import all_components as ext
from objectpack.ui import BaseEditWindow


class UserAddWindow(BaseEditWindow):
    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в :attr: `self`.
        """
        super()._init_components()

        self.field__password = ext.ExtStringField(
            label="password",
            name="new_password",
            allow_blank=True,
            anchor="100%",
            input_type="password",
        )

        self.field__last_login = ext.ExtDateField(
            label="last login",
            name="last_login",
            allow_blank=True,
            anchor="100%",
            format="d.m.Y",
        )
        self.field__is_superuser = ext.ExtCheckBox(
            label="superuser status", name="is_superuser"
        )
        self.field__username = ext.ExtStringField(
            label="username", name="username", allow_blank=False, anchor="100%"
        )
        self.field__first_name = ext.ExtStringField(
            label="first name", name="first_name", allow_blank=False, anchor="100%"
        )
        self.field__last_name = ext.ExtStringField(
            label="last name", name="last_name", allow_blank=False, anchor="100%"
        )
        self.field__email = ext.ExtStringField(
            label="email address", name="email", allow_blank=True, anchor="100%"
        )
        self.field__is_staff = ext.ExtCheckBox(label="staff status", name="is_staff")
        self.field__is_active = ext.ExtCheckBox(label="active", name="is_active")
        self.field__date_joined = ext.ExtDateField(
            label="date joined",
            name="date_joined",
            allow_blank=True,
            anchor="100%",
            format="d.m.Y",
        )

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super()._do_layout()
        self.form.items.extend(
            (
                self.field__password,
                self.field__last_login,
                self.field__is_superuser,
                self.field__username,
                self.field__first_name,
                self.field__last_name,
                self.field__email,
                self.field__is_staff,
                self.field__is_active,
                self.field__date_joined,
            )
        )

    def set_params(self, params):
        """
        Установка параметров окна

        :params: - Словарь c параметрами, передается из пака
        """
        super().set_params(params=params)
        self.height = "auto"
