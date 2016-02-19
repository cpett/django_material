FROM docker.chem.byu.edu:5000/django_base

EXPOSE 80

RUN yum -y install \
  python-devel \
  postgresql \
  postgresql-devel \
  && yum clean all

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app
