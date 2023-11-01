#include "pch.h"
#include "iostream"
#include "CppUnitTest.h"
#include "../lab_6_3_it/lab_6_3_it.cpp"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace lab63ittest
{
	TEST_CLASS(lab63ittest)
	{
	public:
		
		TEST_METHOD(TestMethod1)
		{
			const int n = 5;
			int r[n] = { 5,1,4,3,2 };
			sort(r, n);
			Assert::AreEqual(1, r[0]);
			Assert::AreEqual(2, r[1]);
			Assert::AreEqual(3, r[2]);
			Assert::AreEqual(4, r[3]);
			Assert::AreEqual(5, r[4]);
		}
	};
}
