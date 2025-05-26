CREATE TABLE `nevvon_provider_hashes` (
    `RECORD_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `employee_number` varchar(150) NOT NULL,
    `phone_number` varchar(150) NOT NULL,
    `provider_hash` varchar(150) NOT NULL,
    `org_id` INT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
    deleted_at TIMESTAMP NULL
);
ALTER TABLE `nevvon_provider_hashes`
ADD CONSTRAINT UNIQUE(`org_id`, `employee_number`);