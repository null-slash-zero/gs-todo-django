import React from 'react';
import { Box, Card, Container, Typography } from '@mui/material';

import { TodoListType } from 'todos/types';

type Props = {
  todoList: TodoListType;
};

const TodoListItem: React.FC<Props> = ({ todoList }) => {
  const { name, description } = todoList;
  return (
    <Card>
      <Container sx={{ paddingTop: 2, paddingBottom: 2 }}>
        <Typography variant="h5">{name}</Typography>
        <Box>{description}</Box>
      </Container>
    </Card>
  );
};

export default TodoListItem;
