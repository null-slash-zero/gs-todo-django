import React from 'react';
import { Container, Typography } from '@mui/material';

export interface TitleContainerProps {
  children: React.ReactNode;
  title: string;
  variant?: 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6';
}

const TitleContainer = (
  props: React.PropsWithChildren<TitleContainerProps>
) => {
  const { variant = 'h1' } = props;
  return (
    <>
      <Typography variant={variant} component={variant}>
        {props.title}
      </Typography>
      {props.children}
    </>
  );
};

export default TitleContainer;
