CREATE TABLE parents (parent TEXT, child TEXT);

INSERT INTO parents VALUES
  ('ace', 'bella'),
  ('ace', 'charlie'),
  ('daisy', 'hank'),
  ('finn', 'ace'),
  ('finn', 'daisy'),
  ('finn', 'ginger'),
  ('ellie', 'finn');

CREATE TABLE dogs (name TEXT, fur TEXT, height INTEGER);

INSERT INTO dogs VALUES
  ('ace',     'long',  26),
  ('bella',   'short', 52),
  ('charlie', 'long',  47),
  ('daisy',   'long',  46),
  ('ellie',   'short', 35),
  ('finn',    'curly', 32),
  ('ginger',  'short', 28),
  ('hank',    'curly', 31);

CREATE TABLE sizes (size TEXT, min INTEGER, max INTEGER);

INSERT INTO sizes VALUES
  ('toy',      24, 28),
  ('mini',     28, 35),
  ('medium',   35, 45),
  ('standard', 45, 60);


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT parents.child FROM parents, dogs where dogs.name = parents.parent ORDER BY -dogs.height;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT dogs.name AS name, sizes.size AS size FROM sizes, dogs WHERE dogs.height <= sizes.max AND dogs.height > sizes.min;


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT a.child AS child1, b.child AS child2 FROM parents AS a, parents AS b WHERE a.child < b.child AND a.parent = b.parent;

--The two siblings, bella and charlie, have the same size: standard
-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || siblings.child1 || " and " || siblings.child2 || ", have the same size: " || a.size 
  FROM siblings, size_of_dogs AS a, size_of_dogs AS b 
  WHERE siblings.child1 = a.name AND siblings.child2 = b.name AND a.size = b.size;

-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur, MAX(height) - MIN(height) AS height_range FROM dogs GROUP BY fur HAVING MIN(height) / AVG(height) >= 0.7 AND MAX(height) / AVG(height) <= 1.3;

