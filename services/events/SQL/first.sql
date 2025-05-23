SET @@global.time_zone = '+00:00';
SET time_zone = '+00:00';
CREATE TABLE `smartcare_providers` (
    `smartcare_provider_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nevvon_provider_id` INT,
    `nevvon_org_id` INT NOT NULL,
    `smartcare_id` VARCHAR(50) UNIQUE NOT NULL,
    -- `provider_hash` varchar(150) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
    deleted_at TIMESTAMP NULL
) ENGINE = InnoDB AUTO_INCREMENT = 8 DEFAULT CHARSET = latin1;