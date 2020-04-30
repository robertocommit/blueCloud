from google.cloud import firestore
client = firestore.Client()


def save_temperature(request):
    set_temperature(request)
    return str(get_status())


def set_temperature(request):
    temperature = request.args.get('temperature')
    doc_ref = client.collection('temperatures').document('hc_06__laboratorio')
    doc_ref.set({'temperatura': temperature})


def get_status():
    users_ref = client.collection('temperatures')
    docs = users_ref.get()
    statuses = [i.to_dict() for i in docs][1]
    status = statuses['status']
    return(status)
