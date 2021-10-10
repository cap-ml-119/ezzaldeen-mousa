from enum import Enum
from datetime import datetime
from uuid import uuid4


class Status(Enum):
    DONE = 'DONE'
    PENDING = 'PENDING'
    CANCELD = 'CANCELD'


class Todo():
    # store all tasks in a Dict ( private )
    __TODOS = {}

    def create_task(self, content: str, status: str = Status.PENDING.value):
        """ Create new task with new ID and with specific contents

        Args:
            task_id (str): [unique id for the task]
            content (str): [description for the task]
            created_date (str): [date of creation]
            status (str): [status of task ( DONE, PENDING, CANCELD)]

        Returns:
            [str]: [the ID of the new task ( resently added )]
        """
        task_id = uuid4().hex
        self.__TODOS[task_id] = {
            'content': content,
            'created_date': str(datetime.now()),
            'status': status
        }

        return task_id

    def update_task_content(self, task_id: str, content: str):
        """ Update task content using the IDs of tasks that

        Args:
            task_id (str): id of the required tasks
            content (str): new content

        Returns:
            [Tuple]: [True if the operation successed otherwise False, Error message]
        """
        try:
            self.__TODOS[task_id]['content'] = content
        except:
            return (False, f"Task with id: {task_id}, Doesn't exist.")

        return (True, None)

    def update_task_status(self, task_id: str, status: str):
        """ Update the tasks states and set it to one of these options
        ( DONE, PENDING, CANCELD)

        Args:
            task_id (str): id of the required tasks
            status (str): the new status

        Returns:
            [Tuple]: [True if the operation successed otherwise False, Error message]
        """
        # Should Change this ( Get the list from the Status class )
        Status = ['DONE', 'PENDING', 'CANCELD']
        if status in Status:
            try:
                self.__TODOS[task_id]['status'] = status
            except:
                return (False, f"Cannot update, Task with id: {task_id}, Doesn't exist.")

            return (True, None)
        else:
            return (False, f"The '{status}'' is not from the expeted states")

    def delete_task(self, task_id: str):
        """ delete specific task using ID

        Args:
            task_id (str): id of the required tasks

        Returns:
            Tuple: [True if the operation successed otherwise False, Error message]
        """
        try:
            del self.__TODOS[task_id]
        except:
            return (False, f"Cannot delete, Task with id: {task_id}, Doesn't exist.")

        return (True, None)

    def get_tasks(self):
        """get all the current tasks in the TODOS dictionary

        Returns:
            [dict]: [dict of tasks]
        """
        return self.__TODOS
