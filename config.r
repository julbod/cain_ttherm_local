args <- list(
  drv = RMariaDB::MariaDB(),
  dbname = "viuhydro_wx_data_v2",
  user = "viuhydro_shiny",
  password = ".rt_BKD_SB*Q",
  host = "192.99.62.147",
  port = "3306"
)

args_old_db <- list(
  drv = RMariaDB::MariaDB(),
  dbname = "viuhydro_wx_station_data",
  user = "viuhydro_shiny",
  password = ".rt_BKD_SB*Q",
  host = "192.99.62.147",
  port = "3306"
)
