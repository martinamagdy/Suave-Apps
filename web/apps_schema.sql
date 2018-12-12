-- Create and use customer_db
CREATE DATABASE apps_db;
USE apps_db;

-- Create Two Tables
CREATE TABLE apps (
  name TEXT,
  a_id BIGINT primary key,
  a_size_mb FLOAT,
  a_price FLOAT,
  a_user_rating FLOAT, 
  a_content_rating TEXT,
  a_category TEXT,
  g_size_mb TEXT, 
  g_price TEXT, 
  g_user_rating FLOAT,
  g_content_rating TEXT, 
  g_category TEXT);

CREATE TABLE apple_description(
  id BIGINT primary key,
  track_name TEXT,
  size_bytes BIGINT,
  app_desc TEXT);
