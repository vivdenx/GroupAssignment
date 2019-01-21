#Select Canada
canada <- dataframe %>% 
  filter(country == 'canada')


#Make sure we have all astrological signs, missing ones can be computed by birth date
  #find construction like "for NA in astroligical_sign, compute..."


#Compute distribution of astrological signs within Canadian hockey players & plot
ggplot(data = dataframe) +
  geom_bar(
    stat = 'count',
    mapping = aes(x=astrologicalsign, fill = ?)
  )

