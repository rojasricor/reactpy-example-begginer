from fastapi import FastAPI
from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure

app = FastAPI()


@component
def Task(task):
    counter, set_counter = hooks.use_state(0)

    def handle_click(event):
        set_counter(counter + 1)
        print("clicked")

    if task["priority"] > 1:
        return html.li({
            "key": task["id"],
            "class": "list-group-item list-group-item-action p-1 shadow-lg m-1 rounded-3 fw-light",
        },  html.div({
            "class": "d-flex justify-content-between align-items-center",
        },
            f"⚠️ {task['text']} - {task['priority']}")
        )
    else:
        return html.li({
            "key": task["id"],
            "class": "list-group-item list-group-item-action p-1 shadow-lg m-1 rounded-3 fw-bold",
        }, html.div({
            "class": "d-flex justify-content-between align-items-center",
        },
            f"✅ {task['text']} - {task['priority']} - {counter}",
            html.button({
                "class": "btn btn-danger",
                "on_click": handle_click
            }, "Delete")
        ))


@component
def TaskList():
    tasks = [
        {"id": 0, "text": "Make sure that", "priority": 1},
        {"id": 1, "text": "Everything works", "priority": 2},
        {"id": 2, "text": "Everything is fine", "priority": 3},
        {"id": 3, "text": "Everything is perfect", "priority": 4},
        {"id": 2, "text": "Everything is fine", "priority": 3},
        {"id": 3, "text": "Everything is perfect", "priority": 4},
    ]

    lis = [Task(task) for task in tasks]
    return html.ul({
        "class": "list-group"
    }, lis)


@component
def App():
    return html.main(
        {"class": "container p-5"},
        html.head(
            html.title("My Tasks"),
            html.link(
                {
                    "rel": "stylesheet",
                    "href": "https://cdn.jsdelivr.net/npm/bootswatch@5.3.0/dist/lux/bootstrap.min.css",
                }
            )
        ),
        html.h1("My Tasks List"),
        html.div({
            "class": "row mt-3",
        },
            html.div({"class": "col-md-12"}, TaskList())
        )
    )


configure(app, App)
