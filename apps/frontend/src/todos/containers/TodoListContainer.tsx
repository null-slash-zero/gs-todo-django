import React, { useEffect } from 'react';

import { TODO_LIST_ENDPOINT } from 'base/constants/endpoints';
import useFetch from 'base/hooks/useFetch';

const TodoListContainer = (): React.JSX.Element => {
  const { data, loading, error } = useFetch(TODO_LIST_ENDPOINT, []);

  console.log(data);
  return (
    <div>
      {loading && <p>Loading</p>}
      {data && <p>{data}</p>}
      {error && <p>{error}</p>}
    </div>
  );
};

export default TodoListContainer;
