## this is the code to create the station_meta list used across the website
## for linking station metadata
station_meta = list(
  lowercain = list(name = "Cain Lower",
                   elevation = 1260,
                   startYear = 2019,
                   lat = 50.22562,
                   lon = -126.3567,
                   params = c("RH", "Temp", "Rn_1", "RnTotal", "SDepth", "SDcomp", "SDist_Q", "PYR", "PYRSR", "Telem", "Vtx", "TCase", "Pcp1hr", "Pcp_raw", "Pcp_temp", "SW_SSG", "TA", "SW", "SD", "PC", "VB", "Ib", "Vs", "I_S", "YB", "Ttherm", "Rt"),
                   logos = column(12, align = "center", style='padding:0px;',

                                  logoPics$bcgov_logo,
                                  logoPics$mec_logo,
                                  logoPics$geosci_logo,
                                  logoPics$unlimited_logo,
                                  logoPics$westcoast_logo,
                                  logoPics$mtcain_logo,
                                  logoPics$viac_logo,
                                  logoPics$hes_logo,
                                  logoPics$bcenv_logo,
                                  logoPics$viu_logo,
                                  logoPics$canada_logo)),

  # this station is imported through the old database the raw col defs are : "logstamp","air_temp","rh","wind_spd","wind_spd_max","wind_dir","snow","swe","rain","precip","lys","bp","solar","solar_sw_upper","solar_sw_lower","solar_lw_upper","solar_lw_lower","battery","total_rain","total_precip","rain_12","rain_24","rain_48","rain_72","precip_12","precip_24","precip_48","precip_72"
  cainridgerun = list(name = "Cain Ridge Run",
                      elevation = 1330,
                      startYear = 2019, # is actually 2011 need to append data, but this is diff station...
                      lat = 50.226500,
                      lon = -126.351500,
                      params = c("RH", "Temp", "Mx_Spd", "Mx_Dir", "WSK10mMax", "WDD10mMax", "Wspd", "Dir", "Rn_1", "RnTotal", "SDepth", "SDcomp", "SDist_Q", "PYR", "PYRSR", "Telem", "Vtx", "TCase", "TA", "SD", "VB", "Ib", "Vs", "I_S", "YB", "Ttherm", "Rt"),
                      logos = column(12, align = "center", style='padding:0px;',

                                     logoPics$mec_logo,
                                     logoPics$geosci_logo,
                                     logoPics$unlimited_logo,
                                     logoPics$westcoast_logo,
                                     logoPics$mtcain_logo,
                                     logoPics$viac_logo,
                                     logoPics$hes_logo,
                                     logoPics$bcgov_logo,
                                     logoPics$bcenv_logo,
                                     logoPics$viu_logo,
                                     logoPics$canada_logo))
 )
