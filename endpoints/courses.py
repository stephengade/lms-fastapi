import fastapi
# from database.models import Course, CourseItem
from database.models.courses import Course, CourseItem



router = fastapi.APIRouter()

# import the user types here

courses = []

# start a course
@router.post("/courses")
async def add_course(course: Course):
    courses.append(course)
    return {"message": "Course initiated successfully", "status": "ok"}

# add a playlist item
@router.post("/courses/{course_id}/playlist")
async def add_playlist_item(course_id: int, course_item: CourseItem):
    if 0 <= course_id < len(courses):
        courses[course_id].playlist.append(course_item)
        return {"message": "Item added to playlist successfully", "status":"ok"}
    else:
        return {"message": "Invalid course id", "status": "error"}

# Get all courses
@router.get("/courses", response_model=Course)
async def get_all_courses():
    return {"data": courses, "total_count": len(courses), "status": "ok"}

# Get a course
@router.get("/users/{slug}")
async def get_user_by_id(slug: str):
    ## filter and find the course by the slug
    course = list(filter(lambda x: x.slug == slug, courses))
    return {"data": course, "message": "success", "status": "ok"}


# update a course by id
@router.put("/courses/{course_id}")
async def update_course_by_id(course_id: int, course: CourseItem):
    if 0 <= course_id < len(courses):
        courses[course_id] = course
        return {"message": "Course updated successfully", "status": "ok"}
    else:
        return {"message": "Invalid course id", "status": "error"}
    

# get playlist items by course id

@router.get("/courses/{course_id}/playlist")
async def get_playlist_by_course_id(course_id: int):
    if 0 <= course_id < len(courses):
        return {"data": courses[course_id].playlist, "message": "success", "status": "ok"}
    else:
        return {"message": "Invalid course id", "status": "error"}


# delete a course by id

@router.delete("/courses/{course_id}")
async def delete_course_by_id(course_id: int):
    if 0 <= course_id < len(courses):
        courses.pop(course_id)
        return {"message": "Course deleted successfully", "status": "ok"}
    else:
        return {"message": "Invalid course id", "status": "error"}
    


# delete playlist item by id
@router.delete("/courses/{course_id}/{item_id}")
async def delete_playlist_item(course_id: int, item_id: int):
    return {"message": "Item removed from playlist successfully", "status":"ok"}
