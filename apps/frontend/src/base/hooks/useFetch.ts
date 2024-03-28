import { useState, useEffect } from 'react';
import axios from 'axios';

const useFetch = (
  url: string,
  initialData: any,
  contentType: string = 'application/json'
) => {
  const [data, setData] = useState(initialData);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    axios
      .get(url, { headers: { 'Content-Type': contentType } })
      .then(({ data }) => setData(data))
      .catch((error) => setError(error))
      .finally(() => setLoading(false));
  }, []);

  return { data, loading, error };
};

export default useFetch;
