BEGIN;
CREATE TABLE `dashboard_sentweet` (
    `id` bigint UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `tweet_id` bigint NOT NULL,
    `text` varchar(250) NOT NULL,
    `truncated` bool NOT NULL,
    `lang` varchar(9) NULL,
    `user_id` bigint NOT NULL,
    `user_screen_name` varchar(50) NOT NULL,
    `user_name` varchar(150) NOT NULL,
    `user_verified` bool NOT NULL,
    `created_at` datetime(6) NOT NULL,
    `user_utc_offset` integer NULL,
    `user_time_zone` varchar(150) NULL,
    `filter_level` varchar(6) NULL,
    `latitude` double precision NULL,
    `longitude` double precision NULL,
    `user_geo_enabled` bool NOT NULL,
    `user_location` varchar(150) NULL,
    `favorite_count` integer UNSIGNED NULL,
    `retweet_count` integer UNSIGNED NULL,
    `user_followers_count` integer UNSIGNED NULL,
    `user_friends_count` integer UNSIGNED NULL,
    `in_reply_to_status_id` bigint NULL,
    `retweeted_status_id` bigint NULL,
    `sentiment` integer NOT NULL
);

CREATE TABLE `dashboard_wordscore` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `word` varchar(200) NOT NULL,
    `score` integer NOT NULL,
    `frequency` integer NOT NULL
);

CREATE TABLE `dashboard_stopword` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `word` varchar(200) NOT NULL
);


CREATE INDEX `dashboard_sentweet_fde81f11` ON `dashboard_sentweet` (`created_at`);

COMMIT;
