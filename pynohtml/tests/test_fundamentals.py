import pytest

from ..containers import (
    Area,
    Circle
)

simpleElements_args = [
    (Area, "area"),
    (Circle, "circle")

]


@pytest.mark.parametrize("pynohtmlObject, tag", simpleElements_args)
def test_creationWithoutKwargs(pynohtmlObject, tag):
    expectedResult = "<{TAG}>".format(TAG=tag)
    testValue = pynohtmlObject()
    assert str(testValue) == expectedResult, "{} != {}".format(testValue, expectedResult)


@pytest.mark.parametrize("pynohtmlObject, tag", simpleElements_args)
def test_creationWitKlassSpecified(pynohtmlObject, tag):
    testValue = pynohtmlObject(klass="test_class")
    expectedResult = '<{TAG} class="test_class">'.format(TAG=tag)
    assert str(testValue) == expectedResult, "html result not conform"


@pytest.mark.parametrize("pynohtmlObject, tag", simpleElements_args)
def test_creationWitStyleSpecified(pynohtmlObject, tag):
    testValue = pynohtmlObject(id="test_id")
    expectedResult = '<{TAG} id="test_id">'.format(TAG=tag)
    assert str(testValue) == expectedResult, "html result not conform"


@pytest.mark.parametrize("pynohtmlObject, tag", simpleElements_args)
def test_creationWitStyleAndClass(pynohtmlObject, tag):
    testValue = pynohtmlObject(id="test_id", klass="test_class")
    expectedResult = '<{TAG} class="test_class" id="test_id">'.format(TAG=tag)
    assert str(testValue) == expectedResult, "html result not conform"


@pytest.mark.parametrize("pynohtmlObject, tag", simpleElements_args)
def test_creationWitBoolStyle(pynohtmlObject, tag):
    testValue = pynohtmlObject(checked=True)
    expectedResult = '<{TAG} checked>'.format(TAG=tag)
    assert str(testValue) == expectedResult, "html result not conform"
