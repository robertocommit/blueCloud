from google.cloud import firestore
client = firestore.Client()


def set_status(request):
    status = request.args.get('status')
    doc_ref = client.collection('temperatures').document('hc_06__status')
    doc_ref.set({'status': status})
    return ("OK", 200, {'Access-Control-Allow-Origin': '*'})
