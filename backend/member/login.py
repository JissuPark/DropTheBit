from django.http import HttpResponse
import json

# from MyApplication.MongoDbManager import MongoDbManager

def get_login(request):
    user_id = request.POST('user_id')
    user_pw = request.POST('user_pw')
    # dbUserData = MongoDbManager().get_user_from_db({'user_id':user_id, 'user_pw':user_pw}) -> # 없는 정보면 dbUserData의 리턴값이 null 일지, 아니면 특정한 default의 뭐가 올지 모르겠다.. 우선 if문으로 처리하자
    if dbUserData is None:
        # dbUserData = MongoDbManager().get_user_from_db({'user_id':user_id})
        #if dbUserData is None:
        #    # return HttpResponse("회원정보가 존재하지 않습니다", status = 404)
        #    pass
        #else:
        #    # return HttpResponse("비밀번호가 틀렸습니다", status = 400)
        #    pass
        pass
    else:
        # del dbUserData['_id'] -> 임의로 오는 '_id'라는 것을 지워주고 리턴
        # return HttpResponse(json.dumps(dbUserData), status=200) #그냥 status 값만 보내주면 된다, 나중에 json 삭제 필요
        pass



# 아이디, 비번이 모두 있을 때 - 200
# 아이디만 있을 때 - 400
# 둘 다 없을 때 - 404
# user_id, user_pw로 DB에 쿼리실행
# 리턴 값 있으면 -> status = 200
# 리턴 값 없으면 -> user_id로 DB 쿼리 실행
                # 리턴 있으면 -> status = 400
                # 리턴 없으면 -> status = 404