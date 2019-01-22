library(tidyverse) 
library(plyr) 

#Select only Canada in CLI 
#Make sure we have all astrological signs, missing ones can be computed by birth date 
#find construction like "for NA in astroligical_sign, compute..." 
canadians_adapted <- new_canada_only2 %>% 
  mutate( 
    dates = as.Date(birthDate), 
    months = format(dates,'%m')
  ) 

canadians_adapted$months <- revalue(canadians_adapted$months, c("01"="1")) 
canadians_adapted$months <- revalue(canadians_adapted$months, c("02"="2")) 
canadians_adapted$months <- revalue(canadians_adapted$months, c("03"="3")) 
canadians_adapted$months <- revalue(canadians_adapted$months, c("04"="4")) 
canadians_adapted$months <- revalue(canadians_adapted$months, c("05"="5")) 
canadians_adapted$months <- revalue(canadians_adapted$months, c("06"="6")) 
canadians_adapted$months <- revalue(canadians_adapted$months, c("07"="7")) 
canadians_adapted$months <- revalue(canadians_adapted$months, c("08"="8")) 
canadians_adapted$months <- revalue(canadians_adapted$months, c("09"="9")) 

canadians_adapted2 <- canadians_adapted %>% 
  mutate( 
    month_text = case_when( 
      months == 1 ~ 'January', 
      months == 2 ~ 'February', 
      months == 3 ~ 'March', 
      months == 4 ~ 'April', 
      months == 5 ~ 'May', 
      months == 6 ~ 'June', 
      months == 7 ~ 'July', 
      months == 8 ~ 'August', 
      months == 9 ~ 'September', 
      months == 10 ~ 'October', 
      months == 11 ~ 'November', 
      months == 12 ~ 'December' 
    ) 
  )
canadians_adapted2$abbmonths <- month.abb[canadians_adapted2$months_ordered]
canadians_adapted2$abbmonths <- factor(canadians_adapted2$abbmonths, levels = c("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))

ggplot() +
  geom_bar(data=canadians_adapted2, mapping=aes(x=abbmonths, fill=abbmonths), colour='black') +
  scale_fill_brewer(palette="Set3") +
  scale_fill_discrete(name="Months") +
  labs(title = "Number of Canadian ice hockey players \nbased on their month of birth", x = "Months", y = "Number of players")
