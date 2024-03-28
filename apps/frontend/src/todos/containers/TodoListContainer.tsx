import React from 'react';

import { TODO_LIST_ENDPOINT } from 'base/constants/endpoints';
import useFetch from 'base/hooks/useFetch';

const TodoListContainer = (): React.JSX.Element => {
  const { data, loading, error } = useFetch(TODO_LIST_ENDPOINT, []);

  return (
    <div>
      {loading && <p>Loading</p>}
      {data && <p>Data Loaded</p>}
      {error && <p>Somthing bad happened</p>}
    </div>
  );
};

export default TodoListContainer;
