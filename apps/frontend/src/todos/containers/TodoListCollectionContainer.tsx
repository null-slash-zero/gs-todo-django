import React from 'react';

import { TODO_LIST_ENDPOINT } from 'base/constants/endpoints';
import useFetch from 'base/hooks/useFetch';

import TodoListCollection from 'todos/components/TodoListCollectionComponent';

const TodoListContainer = (): React.JSX.Element => {
  const { data: todoLists, loading, error } = useFetch(TODO_LIST_ENDPOINT, []);

  return (
    <div>
      {loading && <p>Loading</p>}
      {todoLists && <TodoListCollection todoLists={todoLists} />}
      {error && <p>Somthing bad happened</p>}
    </div>
  );
};

export default TodoListContainer;
