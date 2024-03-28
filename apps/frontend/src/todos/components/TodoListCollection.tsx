import React from 'react';
import { Container } from '@mui/material';

import { TodoListItemComponent } from 'todos/components';
import { TodoListType } from 'todos/types';

type Props = {
  todoLists: TodoListType[];
};

const TodoListCollection: React.FC<Props> = ({ todoLists = [] }) => {
  return (
    <Container disableGutters>
      {todoLists.map((todoList: TodoListType) => (
        <TodoListItemComponent key={todoList.id} todoList={todoList} />
      ))}
    </Container>
  );
};

export default TodoListCollection;
