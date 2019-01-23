from Benchmarker import Benchmarker

params = {
    "df_generator": '',
    "functions_to_evaluate": [],
    "title": "Benchmark for pandas df creation",
}

benchmark = Benchmarker(**params)
benchmark.benchmark_time_create_df('pd.DataFrame(np_array, columns=list("AB"))', 'np.random.randint(1, df_size, (df_size, 2))')
