from functools import partial

from django.contrib.auth.models import User
from objectpack.actions import ObjectPack
from objectpack.filters import ColumnFilterEngine, FilterByField
from objectpack.ui import ModelEditWindow


class UserPack(ObjectPack):
    model = User

    filter_engine_clz = ColumnFilterEngine

    f = partial(FilterByField, model)
    # add_window = UserAddWindow
    add_window = ModelEditWindow.fabricate(model=model)

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

    # разрешим добавлять ссылку на list_window в меню Desktop'а
    add_to_menu = True
    add_to_desktop = True
