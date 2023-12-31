from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schema import User_schema, User_update_schema, usercreate_response_serializer, user_response_serializer
from app.services import create_user, get_single_user, update_user, delete_user, get_all_users

app = APIRouter()


# get all persons
@app.get("/api")
async def get_all_persons():
		accounts, Error = get_all_users()

		if Error:
			return JSONResponse(status_code=500, content={"msg":"failed to get users"})
		
		if accounts is None:
			return JSONResponse(status_code=404, content={"msg":"no users found"})
		return [user_response_serializer(account) for account in accounts]

# create a person
@app.post("/api")
async def create_person(request: User_schema):
    account, error = create_user(request)

    if error:
        return JSONResponse(status_code=error.code, content={"msg":error.msg})

    if not account:
        return JSONResponse(status_code=500, content={"msg":"failed to create user"})

    return JSONResponse(content=usercreate_response_serializer(account).model_dump(), status_code=201)


# get a single person
@app.get("/api/{idorname}")
async def get_single_person(idorname: str):
		account, error = get_single_user(idorname)
        
		if error:
			return JSONResponse(status_code=error.code, content={"msg":error.msg})
		if not account:
			return JSONResponse(status_code=404, content={"msg":"user not found"})
		return user_response_serializer(account)

# update a person
@app.put("/api/{idorname}")
async def update_person(idorname: str, request: User_update_schema ):
	account, error = get_single_user(idorname)

	if error:
		return JSONResponse(status_code=error.code, content={"msg":error.msg})
	
	if not account:
		return JSONResponse(status_code=404, content={"msg":"user not found"})
	
	account, error = update_user(
		user_object=account,
		name=request.name,
		)

	if error:
		return JSONResponse(status_code=error.code, content=error.msg)
	
	if not account:
		return JSONResponse(status_code=500, content={"msg":"failed to update user"})
	
	return user_response_serializer(account)

# delete a person
@app.delete("/api/{idorname}")
async def delete_person(idorname: str):
	account, error = get_single_user(idorname)

	if error:
		return JSONResponse(status_code=error.code, content={"msg":error.msg})
	
	if not account:
		return JSONResponse(status_code=404, content={"msg":"user not found"})
	
	account, error = delete_user(account)

	if error:
		return JSONResponse(status_code=error.code, content={"msg":error.msg})
	
	if not account:
		return JSONResponse(status_code=500, content={"msg":"failed to delete user"})
	
	return JSONResponse(status_code=204, content={"msg": "user deleted"})