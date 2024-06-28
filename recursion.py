import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)


def list_tasks(task_hierarchy, indent=0):
   for task in task_hierarchy:
    print(" " * indent + task["name"])
    if "subtasks" in task:
      list_tasks(task["subtasks"], indent + 2)


task_hierarchy_1 = [
    {
        "name": "Project",
        "subtasks": [
            {"name": "Define project scope"},
            {"name": "Create project plan"},
            {"name": "Assign project team",
            "subtasks": [
                {"name": "Identify team members"},
                {"name": "Allocate roles and responsibilities"}
            ]},
            {"name": "Conduct project kickoff meeting"}
        ]
    },
    {
        "name": "Research",
        "subtasks": [
            {"name": "Gather data"},
            {"name": "Analyze data",
            "subtasks": [
                {"name": "Data cleaning"},
                {"name": "Statistical analysis"}
            ]},
            {"name": "Draw conclusions"}
        ]
    }
]

task_hierarchy_2 = [
    {
        "name": "Homework",
        "subtasks": [
            {"name": "Math assignment",
            "subtasks": [
                {"name": "Complete worksheet"},
                {"name": "Study for quiz"}
            ]},
            {"name": "History essay",
            "subtasks": [
                {"name": "Research topic"},
                {"name": "Write essay"}
            ]}
        ]
    },
    {
        "name": "Home project",
        "subtasks": [
            {"name": "Garden renovation",
            "subtasks": [
                {"name": "Design garden layout"},
                {"name": "Purchase plants and materials"}
            ]},
            {"name": "DIY furniture",
            "subtasks": [
                {"name": "Select furniture design"},
                {"name": "Buy materials"},
                {"name": "Assemble furniture"}
            ]}
        ]
    }
]
line_break()
print("Task Hierarchy 1:")
list_tasks(task_hierarchy_1)

line_break()
line_break()

print("\nTask Hierarchy 2:")
list_tasks(task_hierarchy_2)