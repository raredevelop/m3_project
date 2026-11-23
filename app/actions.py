from functools import partial

from django.contrib.auth.models import Group, User
from objectpack.actions import ObjectPack
from objectpack.filters import ColumnFilterEngine, FilterByField
from objectpack.ui import ModelEditWindow


class UserPack(ObjectPack):
    model = User

    filter_engine_clz = ColumnFilterEngine

    f = partial(FilterByField, model)
    # add_window = edit_window = UserAddWindow
    add_window = edit_window = ModelEditWindow.fabricate(model=model)

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
            # "filter": (f("is_staff")),
        },
        {
            "data_index": "is_active",
            "header": "is_active",
            # "filter": (f("is_active")),
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
