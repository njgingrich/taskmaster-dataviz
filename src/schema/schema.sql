CREATE TABLE `seasons` (
  `id` integer UNIQUE PRIMARY KEY,
  `name` text NOT NULL,
  `type` text NOT NULL -- 'regular or champion of champions'
);

CREATE TABLE `episodes` (
  `id` integer UNIQUE PRIMARY KEY,
  `title` text NOT NULL,
  `number` integer NOT NULL, -- 'The episode number within a season',
  `broadcast_date` text NOT NULL -- 'ISO-8601 date'
);

CREATE TABLE `contestants` (
  `id` integer UNIQUE PRIMARY KEY,
  `name` text NOT NULL
);

CREATE TABLE `tasks` (
  `id` integer UNIQUE PRIMARY KEY,
  `title` text NOT NULL,
  `description` text NOT NULL,
  `type` text -- 'prize, group, solo, live, compound, tiebreaker'
);

CREATE TABLE `teams` (
  `id` integer UNIQUE PRIMARY KEY,
  `season_id` integer REFERENCES `seasons` (`id`)
);

CREATE TABLE `contestant_teams` (
  `contestant_id` integer REFERENCES `contestants` (`id`),
  `team_id` integer REFERENCES `teams` (`id`)
);

CREATE TABLE `episode_tasks` (
  `episode_id` integer REFERENCES `episodes` (`id`),
  `task_id` integer REFERENCES `tasks` (`id`),
  `task_order` integer NOT NULL
);

CREATE TABLE `season_contestants` (
  `season_id` integer REFERENCES `seasons` (`id`),
  `contestant_id` integer REFERENCES `contestants` (`id`)
);

CREATE TABLE `task_results` (
  `contestant_id` integer REFERENCES `contestants` (`id`),
  `task_id` integer REFERENCES `tasks` (`id`),
  `team_id` integer DEFAULT null REFERENCES `teams` (`id`),
  `score` integer,
  `bonus` integer DEFAULT null
);

CREATE INDEX `type_index` ON `tasks` (`type`);

CREATE UNIQUE INDEX `contestants_index` ON `contestants` (`id`, `name`);

CREATE UNIQUE INDEX `contestant_teams_index` ON `contestant_teams` (`contestant_id`, `team_id`);

CREATE UNIQUE INDEX `episode_tasks_index` ON `episode_tasks` (`episode_id`, `task_id`);

CREATE UNIQUE INDEX `season_contestants_index` ON `season_contestants` (`season_id`, `contestant_id`);

CREATE UNIQUE INDEX `task_results_index` ON `task_results` (`contestant_id`, `task_id`);
