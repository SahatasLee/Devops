SELECT EXISTS (
   SELECT 1
   FROM information_schema.tables
   WHERE table_schema = '' 
   AND table_name = ''
);