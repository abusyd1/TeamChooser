CREATE TABLE IF NOT EXISTS `Players` (
	`name` VARCHAR(50) NOT NULL,
	`position` VARCHAR(50) NOT NULL,
	`attack_rating` INT NOT NULL,
	`defense_rating` INT, NOT NULL
	`runner` BOOLEAN DEFAULT 'False'
);