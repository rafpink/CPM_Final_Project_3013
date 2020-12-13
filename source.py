import pandas as pd

class CPM:

  def __init__(self, actitity, predecessors, duration):
      '''
      The only imputes are the letter denoting the activity, the predecessors
      of that actitity, and the duration of that actitity
      All calculated values start at zero.
      This is the constructor.
      '''
      self.activity = actitity
      self.predecessors = predecessors
      self.duration = duration
      self.successors = []
      self.es = 0
      self.ef = 0
      self.ls = 0
      self.lf = 0
      self.critical = ''

  def __str__(self):
      '''
      This function allows a string to be returned with the critical path,
      node by node.
      '''
      return self.directpath

  def criticalyesno(self):
      '''
      The float is the amount of days that an activity can by pushed and
      still be able to be finished on time. The critical path is the flow of
      activities where the float of each of them is zero. This means that these
      activities MUST be finished in consecttive order at their assigned
      duration in order to finish on time, implying that the float is zero.
      '''
      self.float = self.lf - self.ef
      if self.lf == self.ef:
          self.critical = 'Y'
      else:
          self.critical = 'N'

def read_data(file_name):
    '''
    The critical path will be calculated using a .CSV file because it is easier
    to import and cleaner to process compared to plugging everything in on
    python itself. To import the .CSV file we will used pandas. A .CSV is used
    becuase it could be made with any text editing program, not just Excel. If
    you prefer to used an .xlsx file, just change pd.read_csv(file) to
    pd.read_excel(file). In theory, you should have the same output. If the file
    name you input is incorrect, the program will give you an error message and
    you will be propted to try again.
    '''
    df = pd.DataFrame()
    while df.empty:
      try:
        df = pd.read_csv(file_name)
        return df
      except FileNotFoundError:
        file_name = input("Incorrect file name. Try again.")

def create_task(mydata):
    '''
    This is one of the most important functions in this code because it puts
    the values from the .CSV file into a list we could work with and iterate
    though. The values are sorted by activity, predecessor, and duration.
    '''
    task_nodes = []
    for i in range(len(mydata)):
        task_nodes.append(CPM(mydata['ACTIVITY'][i],mydata['PREDECESSORS'][i],mydata['DURATION'][i]))
    return task_nodes

def forward(task_nodes):
    '''
    The forward pass determines the early start (ES) and early finish (EF) of
    the critical path. The reason its called the forward pass is because you
    iterate through the activities as you normally would, in order. The early
    start is the earliest start time you could have, which is the finish time
    of its latest predecessor. The early finish is the early start plus the
    duration. It is the earliest you could finish, not accounting for the float.
    '''
    for t in task_nodes:
        if type(t.predecessors) is str:
            t.predecessors = t.predecessors.upper()
            earlyfinish = []
            for i in t.predecessors:
                for j in task_nodes:
                    if j.activity == i:
                        earlyfinish.append(j.ef)
                t.es = max(earlyfinish)
            del earlyfinish
        else:
            t.es = 0
        t.ef = t.es + t.duration

def backward(task_nodes):
    '''
    The backward pass determines the late start (LS) and late finish (LF) of
    the critical path. The reason its called the backward pass is because you
    iterate through the activities in reverse order, backwards basically. You
    start with your last task and move on to your first. The late finish is the
    late start plus the duration, meaning that it is the start is that
    latest time the activity could start in order to finish on time to start is
    successors.
    '''
    pre = []
    earlyfinish = []
    for t in task_nodes:
        if type(t.predecessors) is str:
            for i in t.predecessors:
                for j in i:
                    pre.append(i)
                    for k in task_nodes:
                        if k.activity == i:
                            k.successors.append(t.activity)
                        else:
                            pass
        else:
            pass
        earlyfinish.append(t.ef)

    for t in reversed(task_nodes):
        latestart = []
        if t.activity not in pre:
            t.lf = max(earlyfinish)
        else:
            for l in t.successors:
                for m in (task_nodes):
                    if m.activity == l:
                        latestart.append(m.ls)
            t.lf = min(latestart)
            del latestart
        t.ls = t.lf - t.duration

def float(task_nodes):
    '''
    For every task we have in the list of lists, we will run a loop to have the
    function calculate the float. This runs the function we formulated initially
    but it is done after the forward and backward passes because we need the ES,
    EF, LS, and LF to calculate it.
    '''
    for task in task_nodes:
        task.criticalyesno()

def update_df(df, task_nodes):
    '''
    This function would fill in the missing values and displays it within
    Python. We use the same parameters as in the create_task function. However,
    there are additional parameters that are added as they are calculated
    within this program.
    '''
    df2 = pd.DataFrame({
    'ACTIVITY':df['ACTIVITY'],
    'PREDECESSORS':df['PREDECESSORS'],
    'DURATION':df['DURATION'],
    'ES':pd.Series([task.es for task in task_nodes]),
    'EF':pd.Series([task.ef for task in task_nodes]),
    'LS':pd.Series([task.ls for task in task_nodes]),
    'LF':pd.Series([task.lf for task in task_nodes]),
    'FLOAT':pd.Series([task.float for task in task_nodes]),
    'IS_CRITICAL?':pd.Series([task.critical for task in task_nodes]),
    })
    return df2

def compute_path(task_nodes):
    '''
    This function returns a list that shows the critical path pointing from one
    node to the next. It uses the function from the float calculation and if the
    criticalyesno function exports "Y" as an answer, the activity letter for
    that node will be recorded.
    '''
    directpath = []
    for path in task_nodes:
        if path.critical == 'Y':
            directpath.append(path.activity)
    return directpath

def main():
    '''
    The main function puts all the calls into one other function to make it
    simply look cleaner. Instead of calling all your functions one by one, you
    could run your main function in the test.py file.
    '''
    file_name = input("Please input the file name.\n(Don't forgot to input the file extension. For example, .CSV or .XLSX)")
    df = read_data(file_name)
    task_created = create_task(df)
    forward(task_created)
    backward(task_created)
    float(task_created)
    print(update_df(df, task_created))
    print('\nCritical Path:', ' --> '.join(compute_path(task_created)))
