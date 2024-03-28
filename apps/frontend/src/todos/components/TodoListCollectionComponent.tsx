import React from 'react';

import { TodoListType } from 'todos/types';

type Props = {
  todoLists: TodoListType[];
};

const TodoListCollection: React.FC<Props> = ({ todoLists = [] }) => {
  return (
    <div>
      {todoLists.map((todoList: TodoListType) => (
        <div key={todoList.id}>
          <h3>{todoList.name}</h3>
          <p>{todoList.description}</p>
        </div>
      ))}
    </div>
  );
};

export default TodoListCollection;
