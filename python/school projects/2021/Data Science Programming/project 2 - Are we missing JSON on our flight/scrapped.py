def q2:
      months = ["January",'February','March','April','May','June','July','August','September','October','November','December']

        count = 0
        for airport in self.airportCodeList:
            data_counts = []
            airports = []

            for month in months:
                month_data = self.data.query(f"month == '{month}' & airport_code == '{airport}'")
                delays = month_data['num_of_delays_total'].sum()
                data_points = month_data['num_of_delays_total'].count()
                if delays == int and data_points == int:
                    
                    data_entry = round(delays/data_points)
                    data_counts.append(data_entry)
                    airports.append(month_data["airport_name"])



            dataframe = {'Month': months,"Average Number of Flight Delays":data_counts,"airport_name":airports}
            df = pd.DataFrame(data = dataframe)

            if count == 0:
                chart = (alt.Chart(df,title="Flight Delays by month")
                    .encode(
                        alt.X('Month'),
                        y="Average Number of Flight Delays",
                        color =alt.Color('airport_name',legend=alt.Legend(title="Airport")))
                        .mark_line()
                )
                count += 1

            else:
                chart_segment = (alt.Chart(df,title="Flight Delays by month")
                    .encode(
                        alt.X('Month'),
                        y="Average Number of Flight Delays",
                        color =alt.Color('airport_name',legend=alt.Legend(title="Airport")))
                        .mark_line()
                )

                chart += chart_segment
        print(chart)

        filename = "test.png"
        save(chart,filename)