SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema open_food_fact
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema open_food_fact
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `open_food_fact` DEFAULT CHARACTER SET utf8 ;
USE `open_food_fact` ;

-- -----------------------------------------------------
-- Table `open_food_fact`.`categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `open_food_fact`.`categories` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `open_food_fact`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `open_food_fact`.`products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `generic_name` VARCHAR(100) NULL,
  `nutriscore` VARCHAR(45) NULL,
  `store` VARCHAR(45) NULL,
  `url` VARCHAR(255) NULL,
  `categories_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_products_categories`
    FOREIGN KEY (`categories_id`)
    REFERENCES `open_food_fact`.`categories` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_products_categories_idx` ON `open_food_fact`.`products` (`categories_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `open_food_fact`.`substitute_choose`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `open_food_fact`.`substitute_choose` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `products_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_substitute_choose_products1`
    FOREIGN KEY (`products_id`)
    REFERENCES `open_food_fact`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_substitute_choose_products1_idx` ON `open_food_fact`.`substitute_choose` (`products_id` ASC) VISIBLE;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
