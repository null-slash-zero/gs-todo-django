import React from 'react';
import { TitleContainer } from 'base/containers';

import { TODO_LIST_ENDPOINT } from 'base/constants/endpoints';
import useFetch from 'base/hooks/useFetch';

import { TodoListCollectionComponent } from 'todos/components';

const TodoListContainer = (): React.JSX.Element => {
  const { data: todoLists, loading, error } = useFetch(TODO_LIST_ENDPOINT, []);

  return (
    <TitleContainer title="Todo List" variant="h3">
      {loading && <p>Loading</p>}
      {todoLists && <TodoListCollectionComponent todoLists={todoLists} />}
      {error && <p>Somthing bad happened</p>}
    </TitleContainer>
  );
};

export default TodoListContainer;
