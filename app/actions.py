from functools import partial

from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack
from objectpack.filters import ColumnFilterEngine, FilterByField
from objectpack.ui import ModelEditWindow

from app.controller import observer
from app.ui import UserAddWindow


class UserPack(ObjectPack):
    model = User

    filter_engine_clz = ColumnFilterEngine

    f = partial(FilterByField, model)
    add_window = edit_window = UserAddWindow
    # add_window = edit_window = ModelEditWindow.fabricate(model=model)

    add_to_menu = True
    add_to_desktop = True

    columns = [  # noqa: RUF012
        {
            "data_index": "username",
            "header": "username",
            "searchable": True,
            "sortable": True,
            "filter": (f("username")),
        },
        {
            "data_index": "first_name",
            "header": "first_name",
            "filter": (f("first_name")),
        },
        {
            "data_index": "last_name",
            "header": "last_name",
            "filter": (f("last_name")),
        },
        {
            "data_index": "email",
            "header": "email",
            "filter": (f("email")),
        },
        {
            "data_index": "is_staff",
            "header": "is_staff",
        },
        {
            "data_index": "is_active",
            "header": "is_active",
        },
        {
            "data_index": "date_joined",
            "header": "date_joined",
            "filter": (
                f("date_joined", "date_joined__gte", tooltip="С")
                & f("date_joined", "date_joined__lte", tooltip="По")
            ),
        },
    ]


class GroupPack(ObjectPack):
    model = Group

    filter_engine_clz = ColumnFilterEngine
    f = partial(FilterByField, model)
    add_window = edit_window = ModelEditWindow.fabricate(model=model)

    add_to_menu = True
    add_to_desktop = True

    columns = [  # noqa: RUF012
        {
            "data_index": "name",
            "header": "name",
            "searchable": True,
            "sortable": True,
            "filter": (f("name")),
        },
    ]


class PermissionPack(ObjectPack):
    model = Permission

    filter_engine_clz = ColumnFilterEngine
    f = partial(FilterByField, model, model_register=observer)
    add_window = edit_window = ModelEditWindow.fabricate(
        model=model, model_register=observer
    )

    add_to_menu = True
    add_to_desktop = True

    columns = [  # noqa: RUF012
        {
            "data_index": "__str__",
            "header": "Наименование",
        },
    ]


class ContentTypePack(ObjectPack):
    model = ContentType

    filter_engine_clz = ColumnFilterEngine
    f = partial(FilterByField, model)
    add_window = edit_window = ModelEditWindow.fabricate(model=model)

    add_to_menu = True
    add_to_desktop = True

    columns = [  # noqa: RUF012
        {"data_index": "__str__", "header": "Наименование", "hidden": True},
        {
            "data_index": "app_label",
            "header": "app_label",
            "searchable": True,
            "sortable": True,
            "filter": (f("app_label")),
        },
        {
            "data_index": "model",
            "header": "model",
            "searchable": True,
            "sortable": True,
            "filter": (f("model")),
        },
    ]
