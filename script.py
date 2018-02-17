import pandas as pd
import numpy as np
import glob

JOB_END_INDEX = 1;
CORE_USAGE_INDEX = 5;

workload = np.zeros(shape=(360+1))
path = "/Users/zeenat/Desktop/fragmented_task_usage/*.csv"

for fname in sorted(glob.glob(path)):
    print fname;
    data = pd.read_csv(fname, header=None);

    # job_end = data.loc[JOB_END_INDEX];
    # core_usage = data.loc[CORE_USAGE_INDEX];

    for (idx, row) in data.iterrows():
        slot = int(round ( row.loc[JOB_END_INDEX]/300000000 ));
        print slot;
        workload[slot] = workload[slot]+row.loc[CORE_USAGE_INDEX];
        # print 'slot:', slot, "load: ",workload[slot]


df_out = pd.DataFrame(workload)
df_out.to_csv("/Users/zeenat/Desktop/workload.csv")